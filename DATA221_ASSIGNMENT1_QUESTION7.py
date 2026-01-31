# Harris Khan
# January 29, 2026
# DATA221, Assignment 1, Question 7

# Define a function that converts any number of seconds into its corresponding hours, minutes, remaining seconds, and half of day
def time_converter(total_seconds):

    # If the given seconds is an integer and positive, proceed with the calculations
    if total_seconds == int(total_seconds) and total_seconds >= 0:

        # To handle seconds that may be larger than a day, use modulo to "start a new day". Limits seconds to 86400 seconds
        seconds_since_midnight = total_seconds % 86400

        # Calculate time conversions:

        # Floor divide seconds since midnight by the number of seconds in an hour to find hours since midnight
        hours_since_midnight = (seconds_since_midnight // 3600)

        # Calculate seconds left after the latest hour
        seconds_after_hour = seconds_since_midnight - 3600 * hours_since_midnight

        # Floor divide remaining seconds by number of seconds in a minute to find the minutes after hour
        minutes_after_hour = seconds_after_hour // 60

        # Calculate the seconds left after the latest minute
        seconds_after_minute = seconds_after_hour - 60 * minutes_after_hour

        # Store the value of whether we are in AM or PM
        am_or_pm = ""

        # If we are not past noon
        if hours_since_midnight < 12:

            # Set the time to AM
            am_or_pm = "AM"
        else: # Otherwise, since we are at or past noon

            # Set the time to PM
            am_or_pm = "PM"

            # If the time is past the twelfth hour, subtract 12 to keep the 12 hour formatting
            if hours_since_midnight > 12:
                hours_since_midnight -= 12

        # Return the formatted time as a string
        return str(hours_since_midnight) + " " + str(minutes_after_hour) + " " + str(seconds_after_minute) + " " + am_or_pm

    else: # If the given seconds is not an integer or positive, tell the user to input a positive integer
        return "Please input a positive integer to represent seconds."

# Example of time at 12:00 pm
print(time_converter(43200))
