from unittest.mock import Mock
import math
import numpy.testing as npt

def test_sum_shapes():
    mock_shape1 = Mock()
    mock_shape1.get_area.return_value = 10

    mock_shape2 = Mock()
    mock_shape2.get_area.return_value = 13
    my_shapes = [mock_shape1, mock_shape2]
    total_area = sum(shape.get_area() for shape in my_shapes)

    npt.assert_equal(total_area, 23)

def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data_from_data_source
    data_source = Mock()
    data_source.load_inflammation_data.return_value = [[[0, 2, 0]],
                                                      [[0, 1, 0]]]

    result = analyse_data_from_data_source(data_source)
    npt.assert_array_almost_equal(result, [0, math.sqrt(0.25) ,0])
