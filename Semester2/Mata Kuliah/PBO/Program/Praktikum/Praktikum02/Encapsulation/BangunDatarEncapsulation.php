<?php

class BangunDatarEncapsulation {

    private float $panjang;
    private float $lebar;

    public function getPanjang(): float {
        return $this->panjang;
    }

    public function setPanjang(float $panjang): void {
        // setter dengan validasi
        if ($panjang < 1) {
            $this->panjang = 1;
        } else {
            $this->panjang = $panjang;
        }
    }

    // getter dan setter lebar
    public function getLebar(): float {
        return $this->lebar;
    }

    public function setLebar(float $lebar): void {
        // ternary operator
        $this->lebar = $lebar < 1 ? 1 : $lebar;
    }

    // method getLuas
    public function getLuas(): float {
        return $this->panjang * $this->lebar;
    }
}