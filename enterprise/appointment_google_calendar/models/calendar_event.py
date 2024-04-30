# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import uuid

from odoo import models
from odoo.addons.google_calendar.utils.google_calendar import GoogleCalendarService


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    def _compute_videocall_redirection(self):
        """ Creating a videocall redirection link even if there is no videocall location (google meet url) to ensure
        we have a videocall link to display in the chatter record creation message. The google meet url is indeed only accessible
        after the creation of the record, when the related Google Event has been created and a google synchronization
        has been performed.
        """
        events_w_google_url = self.filtered(lambda event: event.videocall_source == 'google_meet')
        for event in events_w_google_url:
            if event.user_id.is_google_calendar_synced():
                if not event.access_token:
                    event.access_token = uuid.uuid4().hex
                event.videocall_redirection = f"{event.get_base_url()}/calendar/videocall/{event.access_token}"
            else:
                event.videocall_redirection = False
        super(CalendarEvent, self - events_w_google_url)._compute_videocall_redirection()

    def write(self, vals):
        # When the google_id is set on the Odoo event (which means the related Google Calendar event has been created),
        # sync the Odoo event to the Google calendar event to retrieve the Google Meet url.
        if 'google_id' in vals and not 'videocall_location' in vals:
            for event in self.filtered(lambda event: event.videocall_source == 'google_meet' and not event.videocall_location):
                self.env.user._sync_single_event(GoogleCalendarService(self.env['google.service']), event, vals['google_id'])
        return super().write(vals)

    def _google_values(self):
        """ Override the base calendar google values to include the following logic:
        - For appointment types that are not configured as google meet: remove the conferenceData
        That way Google will never create a Hangout meeting
        - For appointment types that are configured as google meet: force conferenceData
        To have the inverse behavior, in that case we always want a Hangout meeting to be created
        (Unless another videocall location was manually specified)."""
        values = super()._google_values()
        if not self.appointment_type_id:
            return values
        if self.appointment_type_id.event_videocall_source != 'google_meet':
            values.pop('conferenceData', None)
        elif not self.google_id and not self.videocall_location and not values.get('conferenceData'):
            values['conferenceData'] = {'createRequest': {'requestId': uuid.uuid4().hex}}
        return values
