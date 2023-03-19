from func_TDX import rolling_window, REF, MA, SMA, HHV, LLV, COUNT, EXIST, CROSS, BARSLAST


def method_hs300(df_hs300, start_date='', end_date='') -> int:
    """
    HS300信号的作用是，当信号是0时，当日不买股票，1时买入。传出
    :param df_hs300:
    :param start_date:
    :param end_date:
    :return: 布尔序列
    """
    if start_date == '':
        start_date = df_hs300.index[0]  # 设置为df第一个日期
    if end_date == '':
        end_date = df_hs300.index[-1]  # 设置为df最后一个日期
    df_hs300 = df_hs300.loc[start_date:end_date]
    hs300_close = df_hs300['close']
    hs300_increase_amount = (hs300_close / REF(hs300_close, 1) - 1) * 100
    # hs300_signal = ~(hs300_increase_amount < -1.5) & ~(hs300_increase_amount > 1.5)
    hs300_signal = ~(hs300_increase_amount < -1.5) & ~(hs300_increase_amount > 1.5)
    return hs300_signal


if __name__ == '__main__':
    a = 0.3
    signal = ~(a < -1.5) & ~(a > 1.5)
    print(signal.iat[-1])
