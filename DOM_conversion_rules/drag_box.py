
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

    # replace 't' with 'text', etc
    df = df.replace('div', 'shape')

    return df
