from pathlib import Path
import math
import pytest

import numpy.testing as npt


def test_analyse_data():
    from inflammation.compute_data import analyse_data

    path = Path.cwd() / "data"

    result = analyse_data(path)

    npt.assert_array_almost_equal(
        result["standard deviation by day"],
        [
            0.0,
            0.22510285714822967,
            0.18157298807917438,
            0.1264422964082338,
            0.9495480975212225,
            0.27118211160458394,
            0.2510471895043333,
            0.22330897462517746,
            0.8968050285648822,
            0.21573875376608442,
            1.242355482565972,
            0.6304209352135726,
            1.5751169611676539,
            2.1885024158255058,
            0.3729574000100042,
            0.6939553833454094,
            2.5236516232301356,
            0.31793119839609973,
            1.2285065710291208,
            1.6314963923941304,
            2.45861227231045,
            1.5555605158651071,
            2.821485304053107,
            0.9211757784564323,
            0.7617697879783256,
            2.1834618812878412,
            0.5536843487265027,
            1.7844163161959075,
            0.2654922053678998,
            1.4393841650828865,
            0.7895976862762704,
            0.649138793201813,
            1.160785440771107,
            0.4241799459465404,
            0.36019113581678774,
            0.8080170725338499,
            0.5032303058647608,
            0.4757466516363618,
            0.45197397977655945,
            0.22070226718532082,
        ],
    )

@pytest.mark.parametrize('data,expected_output', [
        ([[[0, 1, 0], [0, 2, 0]]], [0, 0, 0]),
        ([[[0, 2, 0]], [[0, 1, 0]]], [0, math.sqrt(0.25), 0]),
        ([[[0, 1, 0], [0, 2, 0]], [[0, 1, 0], [0, 2, 0]]], [0, 0, 0])
    ],
    ids=['Two patients in same file', 'Two patients in different files', 
         'Two identical patients in two different files'
    ])

def test_compute_standard_deviation_by_day(data, expected_output):
    from inflammation.compute_data import compute_standard_deviation_by_day

    result = compute_standard_deviation_by_day(data)
    npt.assert_array_almost_equal(result, expected_output)
