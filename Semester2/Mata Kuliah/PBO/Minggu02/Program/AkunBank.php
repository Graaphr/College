<?php
class AkunBank{
    private $saldo;

    public function __construct($saldoAwal){
        $this->saldo = $saldoAwal;
    }

    public function setor($jumlah){
        $this->saldo += $jumlah;
    }

    public function tarik($jumlah){
        if($jumlah <= $this->saldo){
            $this->saldo -= $jumlah;
        } else {
            echo "Saldo tidak cukup <br>";
        }
    }

    public function lihatSaldo(){
        return $this->saldo;
    }
}

$akun = new AkunBank(100000);
$akun->setor(50000);
$akun->tarik(160000);

echo "Saldo sekarang: " . $akun->lihatSaldo();
?>