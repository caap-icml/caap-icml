
def convert_df(df): 

    # rename the 'tag' column to 'type'
    df = df.rename(columns={'tag': 'type'})

    # add xy & delete left, width, top, height
    df['x1'] = round(df['left']).astype(int)
    df['x2'] = round(df['left'] + df['width']).astype(int)
    df.drop(['left', 'width'], axis=1, inplace=True)
    df['y1'] = round(df['top']).astype(int)
    df['y2'] = round(df['top'] + df['height']).astype(int)
    df.drop(['top', 'height'], axis=1, inplace=True)

    # replace 0 with empty string in 'bool' column
    df['focused'] = df['focused'].replace(0, 'False')
    df['focused'] = df['focused'].replace(1, 'True')
    
    # insert value string to text, if text string is None
    df.loc[(df['text'].str.len() == 0) & (df['value'].str.len() > 0), 'text'] = df['value']

    # replace 'input_radio' with 'radio'
    df = df.replace('input_radio', 'radio')
    # replace 'input_checkbox' with 'radio'
    df = df.replace('input_checkbox', 'checkbox')
    # replace 't' with 'text'
    df = df.replace('t', 'text')
    # replace 'textarea' with 'text_area'
    df = df.replace('textarea', 'text_area')
    # replace 'input_text' with 'input_field'
    df = df.replace('input_text', 'input_field')

    return df
