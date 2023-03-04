from unittest import mock
from mocking.create_tar import create_tarball

@mock.patch('create_tar.os.path.basename')
@mock.patch('create_tar.tarfile.open')
def test_create_tarball(mock_open, mock_basename):
    mock_add = mock.MagicMock()
    mock_open.return_value.__enter__.return_value.add = mock_add
    mock_basename.return_value = '/tmp/cat-in-the-dat'
    create_tarball()
    mock_add.assert_called_with(
        '/tmp/cat-in-the-dat', arcname='/tmp/cat-in-the-dat'
    )