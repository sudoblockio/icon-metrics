from icon_metrics.utils.rpc import debug_getTrace, icx_getTransactionResult


def test_debug_getTrace():
    # tx_hash = "0x902b26151a440ce952cef3fdc50ba1449e2252239434ab3af02e33bdda7cebe1"
    tx_hash = "0x0173ae5acee987d7bce6eb64493fe302b35e4931e3e941d90cc5d96178076abe"
    result = icx_getTransactionResult(tx_hash)
    # debug = debug_getTrace(tx_hash)

    assert isinstance(result, dict)
