from Project.ParseAnnotation import parse_annotation
import pandas as pd
from pandas.util.testing import assert_frame_equal
from mock import MagicMock

test_string="""2002/08/26/big/img_265
3
67.363819 44.511485 -1.476417 105.249970 87.209036  1
41.936870 27.064477 1.471906 184.070915 129.345601  1
70.993052 43.355200 1.370217 340.894300 117.498951  1
"""



def test_parse_annnotation():
    side_effect = test_string.split('\n')
    side_effect.append(None)

    data_dict = {'filename': side_effect[0],
               'ellipse': [side_effect[2], side_effect[3], side_effect[4]]}
    true_df = pd.DataFrame(data_dict)

    mock_file = MagicMock()

    mock_file.readline.side_effect = side_effect
    actual_df = parse_annotation(mock_file)

    assert_frame_equal(true_df, actual_df)

def test_parse2_annnotation():
    test_string2 = test_string + test_string;
    side_effect = test_string2.split('\n')
    side_effect.append(None)

    data_dict = {'filename': side_effect[0],
               'ellipse': [side_effect[2], side_effect[3], side_effect[4]]}
    true_df = pd.DataFrame(data_dict)
    true_df = pd.concat([true_df, true_df])

    mock_file = MagicMock()

    mock_file.readline.side_effect = side_effect
    actual_df = parse_annotation(mock_file)

    assert_frame_equal(true_df, actual_df)
