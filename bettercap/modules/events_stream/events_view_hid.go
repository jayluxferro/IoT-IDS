package events_stream

import (
	"fmt"

	"github.com/bettercap/bettercap/network"
	"github.com/bettercap/bettercap/session"

	"github.com/evilsocket/islazy/tui"
)

func (mod *EventsStream) viewHIDEvent(e session.Event) {
	dev := e.Data.(*network.HIDDevice)
	if e.Tag == "hid.device.new" {
		fmt.Fprintf(mod.output, "[%s] [%s] new HID device %s detected on channel %s.\n",
			e.Time.Format(mod.timeFormat),
			tui.Green(e.Tag),
			tui.Bold(dev.Address),
			dev.Channels())
	} else if e.Tag == "hid.device.lost" {
		fmt.Fprintf(mod.output, "[%s] [%s] HID device %s lost.\n",
			e.Time.Format(mod.timeFormat),
			tui.Green(e.Tag),
			tui.Red(dev.Address))
	}
}
