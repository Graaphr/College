<?php
class Dosen {

    public $nama;
    public $nip;
    public $mataKuliah;

    public function __construct($nama, $nip, $mataKuliah){
        $this->nama = $nama;
        $this->nip = $nip;
        $this->mataKuliah = $mataKuliah;
    }

    public function tampilkan(){
        echo "Nama: " . $this->nama . "<br>";
        echo "NIP: " . $this->nip . "<br>";
        echo "Mata Kuliah: " . $this->mataKuliah . "<br>";
    }
}

$dosen1 = new Dosen("Andi Wijaya","123456","Pemrograman Web");
$dosen1->tampilkan();
?>