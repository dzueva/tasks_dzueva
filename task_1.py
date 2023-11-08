#!/usr/bin/env python3

def time_convert(time: str) -> str:
    hour = int(time.split(":")[0])
    minute = int(int(time.split(":")[1]) / 6)
    return f"{hour}.{minute}"


def main():
    events_card = {"time for breakfast": [7, 8],
                   "time for launch": [12, 13],
                   "time for dinner": [18, 19]}
    input_time = str(input("Please, input your time: "))

    float_time = float(time_convert(input_time))
    for event in events_card:
        event_min = events_card[event][0]
        event_max = events_card[event][-1]
        if event_min <= float_time <= event_max:
            print(event)
            break


if __name__ == "__main__":
    main()
