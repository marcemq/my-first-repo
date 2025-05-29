import matplotlib.pyplot as plt
import numpy as np

def generate_data():
    """Generates x values and their squared values"""
    x = np.linspace(-10, 10, 100)
    y = x ** 2
    return x, y

def plot_data(x, y):
    """Plots y = x^2"""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="y = x²", color='purple')
    plt.title("Plot of y = x²")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid(True)
    plt.legend()
    # Save the figure
    plt.savefig("plot.png")
    plt.show()

def main():
    print("Generating and plotting y = x²...")
    x, y = generate_data()
    plot_data(x, y)

if __name__ == "__main__":
    main()
