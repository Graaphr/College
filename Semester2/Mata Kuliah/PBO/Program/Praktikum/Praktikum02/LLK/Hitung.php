<?php

class Hitung {

    public $jariJari;
    public $jarak;
    public $waktu;

    // Fungsi menghitung luas lingkaran
    public function getLuasLingkaran() {
        return pi() * pow($this->jariJari, 2);
    }

    // Fungsi menghitung kecepatan
    public function getKecepatan() {
        if ($this->waktu == 0) {
            return "Input Salah!";
        }
        return $this->jarak / $this->waktu;
    }
}