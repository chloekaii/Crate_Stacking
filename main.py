import time


def stack_crates(n, A, B, C, file):
    if n == 1:
        file.write(f"Move crate {n} from rack {A} to rack {C}\n")
        return
    stack_crates(n - 1, A, C, B, file)
    file.write(f"Move crate {n} from rack {A} to rack {C}\n")
    stack_crates(n - 1, B, A, C, file)


def measure_runtime():
    times = []
    for n in range(1, 21):
        start_time = time.time()
        with open("output.txt", "w") as file:
            stack_crates(n, "A", "B", "C", file)
        end_time = time.time()
        times.append((n, end_time - start_time))
    return times


def save_runtime_plot():
    import matplotlib.pyplot as plt
    runtimes = measure_runtime()
    n_values, time_values = zip(*runtimes)
    plt.plot(n_values, time_values, marker='o', linestyle='-')
    plt.xlabel('Number of Crates (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Runtime Analysis of Crate Stacking Algorithm')
    plt.grid(True)
    plt.savefig('runtime_plot.png')
    plt.show()


if __name__ == '__main__':
    n = int(input("Enter number of crates: "))
    with open("output.txt", "w") as file:
        stack_crates(n, "A", "B", "C", file)
    # save_runtime_plot() #<- commented out for more efficient runtime

