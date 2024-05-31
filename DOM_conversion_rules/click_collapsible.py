from DOM_conversion_rules import convert_df_base_formatting


def convert_df(df):
    df = convert_df_base_formatting(df)

    # replace 't' with 'text'
    df = df.replace('div', 'text')
    df = df.replace('span', 'hyperlink')
    df = df.replace('h3', 'button')

    return df
