import io
import os
import random


def read_tasks():
    result = []
    total_tasks = len(os.listdir('text/tasks'))
    print(total_tasks + 1)

    for i in range(1, total_tasks):
        result.append([])
        total_variants = len(os.listdir('text/tasks/%d' % i))

        for k in range(1, total_variants):
            result[i - 1].append(read_file('text/tasks/%d/%d.tex' % (i, k)))

    return result


def read_students():
    with io.open("students.txt", encoding='utf-8') as file:
        result = file.readlines()

    return result


def generate_variants(tasks, total):
    counts = [len(i) for i in tasks]
    result = set()

    while len(result) < total:
        result.add(generate_variant(counts))

    return list(result)


def generate_variant(counts):
    return tuple(random.randint(1, count) for count in counts)


def read_file(name):
    try:
        with io.open(name, encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {name} not found.")
        return ''


def main():
    random.seed(1183)

    print("Reading templates...")
    head = read_file('templates/head.tex')
    q_start = read_file('templates/qStart.tex')
    q_start2 = read_file('templates/qStart2.tex')
    q_finish = read_file('templates/qFinish.tex')
    tail = read_file('templates/tail.tex')

    print("Reading tasks...")
    tasks = read_tasks()

    print("Reading students...")
    students = read_students()

    print("Generating variants...")
    variants = generate_variants(tasks, len(students))
    random.shuffle(variants)

    os.makedirs(os.path.dirname("text/latex/main.tex"), exist_ok=True)

    with io.open("text/latex/main.tex", "w", encoding='utf-8') as out:
        print("Making main.tex file...")
        out.write(head)

        for i in range(len(variants)):
            out.write(q_start + str(students[i]) + q_start2)

            for task_number, task in enumerate(tasks):
                out.write(task[variants[i][task_number] - 1])

            out.write(q_finish)

        out.write(tail)

    with io.open("text/latex/dump.tex", "w", encoding='utf-8') as out:
        print("Making dump.tex file...")
        out.write(head)

        for i in range(len(tasks)):
            out.write(q_start + str(i + 1) + q_start2)

            for k in range(len(tasks[i])):
                out.write(tasks[i][k])

            out.write(q_finish)

        out.write(tail)

    print("Done!")


if __name__ == "__main__":
    main()
