# TicketMonitor

TicketMonitor is a versatile and customizable tool designed for monitoring screen pixels, automating clicks, and sending alerts based on user-defined conditions. It is perfect for tracking ticket releases, monitoring webpage updates, and automating repetitive tasks.

## File: ticket_checker.py

**Usage**: The purpose of this tool is to monitor a ticket website that releases tickets at random times. Without this tool, users would need to manually refresh their browsers, navigate to the ticket availability page, and check for available tickets (indicated by a blue icon, as opposed to a grey one). TicketMonitor automates this process by simulating mouse click events, navigating to the ticket availability page, checking the icon color, and sending an alert if an available ticket is detected.

**Areas for improvement**: While the current implementation is functional, there are several aspects that could be enhanced:

1. Enhance decision logic by accounting for every possible case, such as:
   - Handling page timeouts and required logins by identifying the appropriate page and responding accordingly.
   - In case of encountering an unexpected situation, restarting the process from the beginning.
2. Instead of merely sending a notification, consider automating additional clicks to complete the booking process.

## File: get_mouse_position.py

This file serves as a helper for `ticket_checker.py` and provides information on the position of specific pixels.

**Usage**: Run `ticket_checker.py`, and it will record the position of each mouse click. Double-click to end the program.
