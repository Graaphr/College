<?php

class Bus {

    private int $jumlahPenumpang = 0;
    private int $kapasitas = 0;

    // Fungsi untuk menentukan besaran kapasitas
    public function setKapasitas(int $kapasitas): void {
        if ($kapasitas > 0) {
            $this->kapasitas = $kapasitas;
        } else {
            echo "Kapasitas Tidak Boleh Kosong" . PHP_EOL;
        }
    }

    // fungsi untuk mengetahui jumlah penumpang
    public function getJumlahPenumpang(): int {
        return $this->jumlahPenumpang;
    }

    // Fungsi untuk mengetahui kapasitas
    public function getKapasitas(): int {
        return $this->kapasitas;
    }

    // Fungsi untuk menambahkan penumpang
    public function tambahPenumpang(int $jumlah): void {
        if ($this->jumlahPenumpang + $jumlah > $this->kapasitas) {
            echo "! Penumpang Melebihi Kapasitas !" . PHP_EOL;
        } else {
            $this->jumlahPenumpang += $jumlah;
            echo "$jumlah Penumpang Naik" . PHP_EOL;
        }
    }

    // Fungsi untuk mengurangi penumpang
    public function kurangiPenumpang(int $jumlah): void {
        if ($this->jumlahPenumpang - $jumlah < 0) {
            echo "Jumlah Penumpang Tidak Boleh Minus" . PHP_EOL;
        } else {
            $this->jumlahPenumpang -= $jumlah;
            echo "$jumlah Penumpang Turun" . PHP_EOL;
        }
    }
}