from download_off_snapshot import (
    download_snapshot,
)

from filter_estonia_products import (
    filter_estonia_products,
)


def create_bootstrap_dataset():
    """
    Bootstrap workflow:

    OFF snapshot
    → Estonia filtering
    → bootstrap parquet
    """

    print("=== Bootstrap workflow started ===")

    print("\n[1/2] OFF snapshot download")

    download_snapshot()

    print("\n[2/2] Estonia bootstrap generation")

    filter_estonia_products()

    print("\n=== Bootstrap workflow completed ===")


if __name__ == "__main__":
    create_bootstrap_dataset()
