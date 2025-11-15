import re
import pandas as pd

def preprocess(data):

    # Pattern that matches BOTH: 12/11/25, 21:55 -  AND 12/11/2025, 21:55 -
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Try long year first, if it fails use short year
    try:
        df['message_date'] = pd.to_datetime(df['message_date'],
                                            format='%d/%m/%Y, %H:%M - ')
    except:
        df['message_date'] = pd.to_datetime(df['message_date'],
                                            format='%d/%m/%y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    # split user & message
    users = []
    msgs = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            msgs.append(" ".join(entry[2:]))
        else:
            users.append("group_notification")
            msgs.append(entry[0])

    df["user"] = users
    df["message"] = msgs
    df.drop(columns=["user_message"], inplace=True)

    # datetime breakdowns
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # period generation
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append(f"{hour}-00")
        elif hour == 0:
            period.append(f"00-{hour+1}")
        else:
            period.append(f"{hour}-{hour+1}")

    df['period'] = period

    return df
