{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNKdSL0rD2q4W96igJslbuY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/Tegar348/Jobsheet-09-Modular-Programming-Import-From-Library-Standar-/blob/main/modulku.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ceffc25",
        "outputId": "3bcb528c-8383-436b-b67a-a31f1aeafb32"
      },
      "source": [
        "%%writefile modulku.py\n",
        "halo = \"Halo, Dunia!\"\n",
        "\n",
        "def halo(nama):\n",
        "  return f\"Halo, {nama}!\""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting modulku.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def halo(nama):\n",
        "  print(f\"Halo, {nama}! Selamat belajar Python di Polines.\")\n",
        "\n",
        "import modulku\n",
        "\n",
        "modulku.halo(\"Mahasiswa Polines\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "cdscA6xPlftD",
        "outputId": "24f77d3f-1c4b-4d81-d1e8-7baa1892ba61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Halo, Mahasiswa Polines!'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    }
  ]
}