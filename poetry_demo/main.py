import sys
import numpy as np
import matplotlib.pyplot as plt


def main() -> int:
    """メイン関数

    Returns:
        int: 正常終了時は0を返す
    """
    # 整数型の配列を用意
    arr_int32 = np.array([100, 200, 300, 400, 500], dtype=np.int32)
    print(arr_int32)

    # 浮動小数点型の配列を用意
    arr_float = np.array([0.1, 0.2, 0.3, 0.4, 0.5], dtype=np.float64)
    print(arr_float)

    # 行列計算
    arr_sum = arr_int32 + arr_float
    print(arr_sum)

    # データ作成
    x = np.linspace(0, 10, 100)
    y = x + np.random.randn(100)

    # プロット
    plt.plot(x, y, label="Test")

    # 凡例
    plt.legend()

    # 表示
    plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main())
