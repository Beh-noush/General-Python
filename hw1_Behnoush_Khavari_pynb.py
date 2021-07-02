{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "hw1_Behnoush_Khavari.pynb.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Beh-noush/General-Python/blob/main/hw1_Behnoush_Khavari_pynb.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z8p_rVKVWH2w"
      },
      "source": [
        "# IFT6269 -  Maximum Likelihood Estimation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SloWv9XFBdxL"
      },
      "source": [
        "### Introduction\n",
        "W\n",
        "e are going to numerically explore the MLE of the variance parameter of the Gaussian."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WlK2DyIsTCEk"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UbbWroVpRo-R"
      },
      "source": [
        "def sample_gaussian_data(num_samples, num_trials):\n",
        "  \"\"\"\n",
        "  inputs: \n",
        "     num_samples: [int] number of samples to generate for each trial\n",
        "     num_trials: [int] number of trials\n",
        "  Returns:\n",
        "     samples: [num_samples,num_trial] Array of generated samples.\n",
        "  \"\"\"\n",
        "  return np.random.randn(num_samples, num_trials)"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RfzZh9OwTy8g"
      },
      "source": [
        "def mu_sigma2_mle(samples):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Compute Gaussian MLE estimators for the mean and variance \n",
        "        Inputs:\n",
        "             samples: [num_samples, num_trials] Matrix of N(0, 1) iid samples. \n",
        "                      It contains num_trials sets, each of these sets containing\n",
        "                      num_samples samples.\n",
        "        \n",
        "        Returns:\n",
        "             mu_hat: [num_trials] Vector of MLE mean estimators for each trial\n",
        "             sigma2_hat: [num_trials] Vector of MLE variance estimators for each trial\n",
        "             \n",
        "    \"\"\"\n",
        "    mean = np.mean(samples , axis = 0)\n",
        "    var = np.mean( (samples - mean)**2, axis = 0 )\n",
        "    return mean , var "
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ur_MyJhzXSWq"
      },
      "source": [
        "def freq_mean_var(x):\n",
        "    \"\"\"\n",
        "    Compute the frequentist mean and variance of a vector of n real numbers \n",
        "        Inputs:\n",
        "             x: [n] Vector of real numbers\n",
        "        \n",
        "        Returns:\n",
        "             (mean, var): [tuple] Frequentist mean and variance of x\n",
        "             \n",
        "    \"\"\"\n",
        "    mean = np.mean(x)\n",
        "    var = np.mean((x - mean)**2)\n",
        "    return (mean , var)\n"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-2Bqj64ZTy3X"
      },
      "source": [
        "def empirical_frequentist_bias(empirical_mean, true_mean):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Estimate the frequentist bias of an estimator given its empirical and true means \n",
        "        Inputs:\n",
        "             true_mean: [float] True mean of the estimator\n",
        "             empirical_mean: [float] Empirical mean of the estimator\n",
        "             \n",
        "        Returns:\n",
        "             bias: [float] Frequentist bias\n",
        "            \n",
        "    \"\"\"\n",
        "    return true_mean - empirical_mean\n"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QLChG0awZMOd"
      },
      "source": [
        "def plot_sigma_hat_histogram(samples, bins=200):\n",
        "    \"\"\"\n",
        "    Plots a histogram of a estimated variances \n",
        "        Inputs:\n",
        "            samples: [array] Estimated variances to be plotted\n",
        "\n",
        "    \"\"\"\n",
        "    plt.xlabel('variance')\n",
        "    plt.ylabel('counts')\n",
        "    plt.hist(samples, bins )"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yn6zTvnxeae-",
        "outputId": "c40df893-6d48-44ae-bede-3e8631b5b238"
      },
      "source": [
        "#draw  𝑛=5  samples from the standard Gaussian distribution,  N(0,1) .\n",
        "samples = sample_gaussian_data(5,1)\n",
        "print(f'Generated Gaussian samples\\n{samples}')"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Generated Gaussian samples\n",
            "[[-1.18890842]\n",
            " [ 0.62134348]\n",
            " [ 0.42917227]\n",
            " [-0.98416142]\n",
            " [ 0.2704691 ]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ohE-Le__ZMoz",
        "outputId": "e7e38f4e-d3b9-46d8-b347-02092cd06437"
      },
      "source": [
        "#Compute the ML estimate  𝜇̂  for the mean and  𝜎̂2  for the variance of the Gaussian, as given in Question 3(d).\n",
        "mean , variance = mu_sigma2_mle(samples)\n",
        "print(f'MLE of mean is {mean}\\nMLE of variance is {variance}') "
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "MLE of mean is [-0.170417]\n",
            "MLE of variance is [0.57605545]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rgTs2nnTnuth"
      },
      "source": [
        "#Repeat the previous steps 10,000 times. Plot a histogram of the 10,000 estimates of the Gaussian variance parameter to show its empirical distribution.\n",
        "variance_list = []\n",
        "for iter in range(10000):\n",
        "  samples = sample_gaussian_data(5 , 1)\n",
        "  mean , var = mu_sigma2_mle(samples)\n",
        "  variance_list.append(var)\n",
        "plot_sigma_hat_histogram(variance_list , bins = 200)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 280
        },
        "id": "EjstCJ0dsheK",
        "outputId": "9a4e6ff0-30e7-4195-8b70-4275ae56d1c2"
      },
      "source": [
        "samples  =  sample_gaussian_data(5 , 10000)\n",
        "mean , var = mu_sigma2_mle(samples)\n",
        "plot_sigma_hat_histogram(var, bins = 200)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "YUiBh13Wpt0q"
      },
      "source": [
        "We notice that the shape of this histogram shows the Chi-square distribution as we expected for the sum of squares of standard normal variables.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1QZYzYg5x-yj",
        "outputId": "b2383764-0564-4050-d594-3b86308952e1"
      },
      "source": [
        "bias_of_gaussian_variance = 1 - np.mean(var) \n",
        "bias_of_gaussian_variance"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.19962312114292557"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aYtO-I5syDou",
        "outputId": "9eb7b65b-2b72-455d-c10b-f7e4d169b8ad"
      },
      "source": [
        "var_of_gaussian_variance = np.mean((var - np.mean(var))**2)\n",
        "var_of_gaussian_variance "
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.31670181055821495"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ic7wSHTOz-c8"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "L15of8ttz-Tn"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vGtfm6nnrpqd"
      },
      "source": [
        "bias_of_gaussian_variance = np.mean(var) - 1\n",
        "\n",
        "# Use the same 10,000 repeated trials to numerically estimate the (frequentist) bias and variance of the ML estimate  𝜎̂2  of the Gaussian variance parameter.\n",
        "# Compare the results with the theoretical (frequentist) bias and variance that you can compute from the formula you derived in Question 3(d).\n",
        "sigma2_hat_mean, sigma2_hat_var = freq_mean_var(sigma2_hat_vec)\n",
        "\n",
        "TRUE_SIGMA2 = 1.\n",
        "\n",
        "# In the next lines, fill in the theoretical bias and variance of $\\hat{\\sigma}^2$\n",
        "n = NUM_SAMPLES\n",
        "THEO_BIAS = TRUE_SIGMA2/n\n",
        "THEO_VAR =  TRUE_SIGMA2**2*(2*n -2)/(n**2)\n",
        "\n",
        "emp_bias = empirical_frequentist_bias(empirical_mean=sigma2_hat_mean,\n",
        "                                      true_mean=TRUE_SIGMA2)\n",
        "\n",
        "print('Theoretical Bias: ', THEO_BIAS, ' Freq. Estimated Bias: ', emp_bias)\n",
        "print('Theoretical Variance: ', THEO_VAR, ' Freq. Estimated Variance: ', sigma2_hat_var)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Naeit-wGuLsm"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QGtWSwUeuLn9"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pJlUxcYmBYCK"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "plt.style.use('seaborn-white')\n",
        "params = {'legend.fontsize': 'x-large',\n",
        "         'axes.labelsize': 'x-large',\n",
        "         'axes.titlesize':'x-large',\n",
        "         'xtick.labelsize':'x-large',\n",
        "         'ytick.labelsize':'x-large'}\n",
        "plt.rcParams.update(params)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EbMexfJ6uxSh"
      },
      "source": [
        "def sample_gaussian_data(num_samples, num_trials):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Generate num_trials sets of samples of a *standard* 1-d Gaussian random variable.\n",
        "    Each set of samples contains num_sample samples\n",
        "\n",
        "        Inputs:\n",
        "            num_samples: [int] Number of samples to generate per trial\n",
        "            num_trials: [int] Number of trials to generate\n",
        "        \n",
        "        Returns:\n",
        "            samples: [num_samples, num_trials] Vector of generated samples\n",
        "    \"\"\"\n",
        "\n",
        "    # TODO\n",
        "    samples = np.transpose(np.random.randn( num_trials, num_samples))\n",
        "\n",
        "    return samples\n",
        "\n",
        "def mu_sigma2_mle(samples):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Compute Gaussian MLE estimators for the mean and variance \n",
        "        Inputs:\n",
        "             samples: [num_samples, num_trials] Matrix of N(0, 1) iid samples. \n",
        "                      It contains num_trials sets, each of these sets containing\n",
        "                      num_samples samples.\n",
        "        \n",
        "        Returns:\n",
        "             mu_hat: [num_trials] Vector of MLE mean estimators for each trial\n",
        "             sigma2_hat: [num_trials] Vector of MLE variance estimators for each trial\n",
        "             \n",
        "    \"\"\"\n",
        "    # Useful dimensions\n",
        "    num_samples, num_trials = samples.shape\n",
        "\n",
        "    #TODO\n",
        "    mu_hat = np.mean(samples,0)\n",
        "    sigma2_hat = np.var(samples,0)\n",
        "\n",
        "    return mu_hat, sigma2_hat\n",
        "\n",
        "def freq_mean_var(x):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Compute the frequentist mean and variance of a vector of n real numbers \n",
        "        Inputs:\n",
        "             x: [n] Vector of real numbers\n",
        "        \n",
        "        Returns:\n",
        "             (mean, var): [tuple] Frequentist mean and variance of x\n",
        "             \n",
        "    \"\"\"\n",
        "\n",
        "    #TODO\n",
        "    mean, var = np.mean(x), np.mean((x-np.mean(x))**2)\n",
        "\n",
        "    return mean, var\n",
        "\n",
        "def empirical_frequentist_bias(empirical_mean, true_mean):\n",
        "    \"\"\"\n",
        "    # TODO \n",
        "    Estimate the frequentist bias of an estimator given its empirical and true means \n",
        "        Inputs:\n",
        "             true_mean: [float] True mean of the estimator\n",
        "             empirical_mean: [float] Empirical mean of the estimator\n",
        "             \n",
        "        Returns:\n",
        "             bias: [float] Frequentist bias\n",
        "            \n",
        "    \"\"\"\n",
        "\n",
        "    #TODO\n",
        "    bias = true_mean - empirical_mean\n",
        "\n",
        "    return bias\n",
        "\n",
        "def plot_sigma_hat_histogram(samples, bins=200):\n",
        "    \"\"\"\n",
        "    Plots a histogram of a estimated variances \n",
        "        Inputs:\n",
        "            samples: [array] Estimated variances to be plotted\n",
        "\n",
        "    \"\"\"\n",
        "    # Plot histogram with custom bins for readability.\n",
        "    plt.hist(samples, bins=bins, alpha=0.8, label=r'$\\hat{\\sigma}$' +' histogram');\n",
        "    plt.ylabel('Counts')\n",
        "    plt.xlabel(r'$\\hat{\\sigma^2}$')\n",
        "    plt.legend();"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Eqmd8My_X6eQ"
      },
      "source": [
        "## Gaussian Maximum Likelihood Estimation\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oMRtEaq8v9U8"
      },
      "source": [
        "### Sample generation\n",
        "\n",
        "Use the functions defined above to draw $n=5$ samples from the standard Gaussian distribution, $\\mathcal{N}(0,1)$."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CV8p-HkJv19I",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        },
        "outputId": "7d06d75d-1e76-4c7c-c675-4bb8d613a0f5"
      },
      "source": [
        "NUM_SAMPLES = 5\n",
        "\n",
        "samples = sample_gaussian_data(num_samples=NUM_SAMPLES, num_trials=1)\n",
        "\n",
        "print('Generated Gaussian samples')\n",
        "print(samples)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Generated Gaussian samples\n",
            "[[-0.96748746]\n",
            " [ 0.3470422 ]\n",
            " [-0.35715657]\n",
            " [ 0.97725692]\n",
            " [ 0.18628083]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CD5_zQ1ywoCR"
      },
      "source": [
        "### MLE computation\n",
        "Compute the ML estimate $\\hat{\\mu}$ for the mean and $\\hat{\\sigma}^2$ for the variance of the Gaussian, as given in Question 3(d). "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2Yhy5FWMt5gE",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "3eb69d9b-0868-40ca-ddf5-a4295b437355"
      },
      "source": [
        "mu_hat, sigma2_hat = mu_sigma2_mle(samples)\n",
        "\n",
        "print('MLE mean - variance')\n",
        "print(mu_hat, sigma2_hat)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "MLE mean - variance\n",
            "[0.03718718] [0.43336966]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OtW53ntTzotm"
      },
      "source": [
        "### MLE computation\n",
        "Repeat the previous steps 10,000 times.  Plot a histogram of the 10,000 estimates of the Gaussian  variance  parameter  to  show  its  empirical  distribution."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vPMfMLQgzyEt"
      },
      "source": [
        "NUM_TRIALS = int(1e4)\n",
        "samples = sample_gaussian_data(num_samples=NUM_SAMPLES, num_trials=NUM_TRIALS)\n",
        "_, sigma2_hat_vec = mu_sigma2_mle(samples)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hoWL_bRJ0U7K",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 292
        },
        "outputId": "fd5c201c-7672-4b15-c656-ecb77cf750d8"
      },
      "source": [
        "plot_sigma_hat_histogram(sigma2_hat_vec)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Wdt6wOYcz0WY"
      },
      "source": [
        "**Question:** Do you recognize the shape of this histogram? What is it? \n",
        "\n",
        "**Answer:** \n",
        "Chi-square distribution as we expected for the sum of squares of standard normal variables.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sGN0em1z0Vif"
      },
      "source": [
        "### Bias and variance of the *estimator*\n",
        "Use *the same* 10,000 repeated trials to numerically estimate the (frequentist) bias and variance of the ML estimate $\\hat{\\sigma}^2$ of the Gaussian variance parameter.\n",
        "\n",
        "Compare the results with the theoretical (frequentist) bias and variance that you can compute from the formula you derived in Question 3(d). \n",
        "\n",
        "*Hint: if your numerical estimates are very far from the theoretical formula, you made a mistake somewhere!*"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yi_qhsg80ATu",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "outputId": "ca8952f9-f69e-412d-8d3e-3a879fb4ce81"
      },
      "source": [
        "sigma2_hat_mean, sigma2_hat_var = freq_mean_var(sigma2_hat_vec)\n",
        "\n",
        "TRUE_SIGMA2 = 1.\n",
        "\n",
        "# In the next lines, fill in the theoretical bias and variance of $\\hat{\\sigma}^2$\n",
        "n = NUM_SAMPLES\n",
        "THEO_BIAS = TRUE_SIGMA2/n\n",
        "THEO_VAR =  TRUE_SIGMA2**2*(2*n -2)/(n**2)\n",
        "\n",
        "emp_bias = empirical_frequentist_bias(empirical_mean=sigma2_hat_mean,\n",
        "                                      true_mean=TRUE_SIGMA2)\n",
        "\n",
        "print('Theoretical Bias: ', THEO_BIAS, ' Freq. Estimated Bias: ', emp_bias)\n",
        "print('Theoretical Variance: ', THEO_VAR, ' Freq. Estimated Variance: ', sigma2_hat_var)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Theoretical Bias:  0.2  Freq. Estimated Bias:  0.20999156088616533\n",
            "Theoretical Variance:  0.32  Freq. Estimated Variance:  0.31670584193825585\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hEIHeZCN5Ogf"
      },
      "source": [
        "**Question:** What conclusions can you draw from the result of this comparison?\n",
        "\n",
        "**Answer:** We see that the numerical result is pretty close to the theoretical one. But it seems that it is a little bit higher that could be a result of intrinsic uncertainty. I don't have more idea on why so!"
      ]
    }
  ]
}