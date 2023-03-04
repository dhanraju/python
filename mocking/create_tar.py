import os
import tarfile


def create_tarball():
    with tarfile.open('/tmp/new_csv_files.tar.gz', 'w:gz') as tar:
        tar.add(
            '/home/dhanu/Downloads/cat-in-the-dat',
            arcname=os.path.basename('/home/dhanu/Downloads/cat-in-the-dat'),
        )


if __name__ == '__main__':
    create_tarball()