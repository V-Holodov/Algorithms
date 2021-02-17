# ID 48164792

def keyboard_trainer(k, trainer):
    uniq_num = set(trainer)
    if '.' in uniq_num:
        uniq_num.remove('.')
    score = sum(1 for num in uniq_num if trainer.count(num) <= k * 2)
    return score


if __name__ == '__main__':
    k = int(input())
    trainer = []
    for i in range(4):
        trainer += input()
    print(keyboard_trainer(k, trainer))
