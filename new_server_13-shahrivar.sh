# finished

done
ek ir gwim s1
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ek_ir_gwim_s1_ham.txt > outputlog_ek_ir_gwim_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ek_ir_gwim_s1_ham.txt

done
ek ir gwim s2
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ek_ir_gwim_s2_ham.txt > outputlog_ek_ir_gwim_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ek_ir_gwim_s2_ham.txt

done
ek ir eigv s1
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s1_ham.txt > outputlog_ekpm_ir_eigv_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_ham.txt

done
ekpm_ir_eigv_prb_s1
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s1_ham.txt > outputlog_ekpm_ir_eigv_prb_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_ham.txt

done
ekpm_ir_eigv_kshell_s1
python -u start.py -c "ekpm_ir_eigv_kshell_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_kshell_s1_ham.txt > outputlog_ekpm_ir_eigv_kshell_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_s1_ham.txt


done
ek ir eigv s2
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s2_ham.txt > outputlog_ekpm_ir_eigv_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_ham.txt

done
ekpm_ir_eigv_kshell_s2
python -u start.py -c "ekpm_ir_eigv_kshell_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_kshell_s2_ham.txt > outputlog_ekpm_ir_eigv_kshell_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_s2_ham.txt

done
ekpm_ir_eigv_prb_s2
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s2_ham.txt > outputlog_ekpm_ir_eigv_prb_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_ham.txt


done
ekpm_ir_eigv_kshell_prb_s1
python -u start.py -c "ekpm_ir_eigv_kshell_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_kshell_prb_s1_ham.txt > outputlog_ekpm_ir_eigv_kshell_prb_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_prb_s1_ham.txt



done
ekpm_ir_eigv_kshell_prb_s2
python -u start.py -c "ekpm_ir_eigv_kshell_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_kshell_prb_s2_ham.txt > outputlog_ekpm_ir_eigv_kshell_prb_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_prb_s2_ham.txt


# tests execution


gwim default
simple
done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/gwim_default_normal_test_ham.txt > outputlog_gwim_default_normal_test_ham.txt 2>&1 &
tail --follow -n 10 results/gwim_default_normal_test_ham.txt


# tests of main article 
done
python -u start.py -c "gwim_default" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/gwim_default_5.3.1.1_ham.txt > outputlog_gwim_default_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.3.1.1_ham.txt

done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/gwim_default_5.3.1.2_ham.txt > outputlog_gwim_default_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.3.1.2_ham.txt


# template
-----
!done
name
python -u start.py -c "" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/_ham.txt > outputlog__ham.txt 2>&1 &
tail --follow -n 10 results/_ham.txt
----



# ekpm default
done
python -u start.py -c "ekpm_default_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s1_5.3.1.1_ham.txt > outputlog_ekpm_default_s1_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.3.1.1_ham.txt

done
python -u start.py -c "ekpm_default_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s2_5.3.1.1_ham.txt > outputlog_ekpm_default_s2_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.3.1.1_ham.txt


done
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s1_5.3.1.2_ham.txt > outputlog_ekpm_default_s1_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.3.1.2_ham.txt

done
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s2_5.3.1.2_ham.txt > outputlog_ekpm_default_s2_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.3.1.2_ham.txt





done
ekpm_default_s1
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s1_ham.txt > outputlog_ekpm_default_s1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_ham.txt

done
ekpm_default_s2
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s2_ham.txt > outputlog_ekpm_default_s2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_ham.txt