import sh


class StellarClient:
    def __init__(self, snapshot_name):
        self.__cli = sh.Command('stellar')
        self.__snapshot_name = snapshot_name

    def create_snapshot(self):
        result = self.__cli('snapshot', self.__snapshot_name)
        return result.exit_code == 0

    def list_snapshots(self):
        result = self.__cli('list')
        return result.exit_code == 0

    def restore_snapshot(self):
        result = self.__cli('restore', self.__snapshot_name)
        return result.exit_code == 0

    def remove_snapshot(self):
        result = self.__cli('remove', self.__snapshot_name)
        return result.exit_code == 0