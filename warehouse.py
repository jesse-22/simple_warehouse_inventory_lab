def warehouse(total, transaction):
    total = dict(total)
    transaction = list(transaction)
    return total, transaction


class WarehouseProcess:
    def __init__(self, total, transaction):
        self.total = dict(total)
        self.transaction = list(transaction)

    def get_transaction(self, transaction):
        return self.transaction[0]

    def process_transaction(self, transaction):
        transaction = self.get_transaction(transaction)
        item = self.transaction[1]
        amount = self.transaction[2]
        if transaction == "receive":
            if item in self.total:
                self.total[item] += amount
                print(self.total)
        if transaction == "ship":
            if item in self.total:
                if self.total[item] == 0:
                    print("Inventory is out of stock")
                else:
                    self.total[item] -= amount
                    print(self.total)


def main():
    total = {'a': 0, 'b': 10}
    transaction = ('ship', 'a', 10)
    warehouse(total, transaction)
    w = WarehouseProcess(total, transaction)
    w.process_transaction(transaction)


if __name__ == "__main__":
    main()
