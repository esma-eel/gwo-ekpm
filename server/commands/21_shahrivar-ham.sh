# ham ekpm_ir_gwim
!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s1_5.3.1.1_ham.txt > outputlog_ekpm_ir_gwim_s1_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.3.1.1_ham.txt

!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s2_5.3.1.1_ham.txt > outputlog_ekpm_ir_gwim_s2_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.3.1.1_ham.txt



!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s1_5.3.1.2_ham.txt > outputlog_ekpm_ir_gwim_s1_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.3.1.2_ham.txt

!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s2_5.3.1.2_ham.txt > outputlog_ekpm_ir_gwim_s2_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.3.1.2_ham.txt


!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s1_5.2_ham.txt > outputlog_ekpm_ir_gwim_s1_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.2_ham.txt


!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_gwim_s2_5.2_ham.txt > outputlog_ekpm_ir_gwim_s2_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.2_ham.txt


# ham ekpm_ir_eigv
!done
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s1_5.3.1.1_ham.txt > outputlog_ekpm_ir_eigv_s1_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.3.1.1_ham.txt

!done
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s2_5.3.1.1_ham.txt > outputlog_ekpm_ir_eigv_s2_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.3.1.1_ham.txt



!done
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s1_5.3.1.2_ham.txt > outputlog_ekpm_ir_eigv_s1_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.3.1.2_ham.txt

!done
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s2_5.3.1.2_ham.txt > outputlog_ekpm_ir_eigv_s2_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.3.1.2_ham.txt


python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s1_5.2_ham.txt > outputlog_ekpm_ir_eigv_s1_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.2_ham.txt


python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_s2_5.2_ham.txt > outputlog_ekpm_ir_eigv_s2_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.2_ham.txt


# ham ekpm_ir_eigv_prb
!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.3.1.1_ham.txt > outputlog_ekpm_ir_eigv_prb_s1_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.3.1.1_ham.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.3.1.1_ham.txt > outputlog_ekpm_ir_eigv_prb_s2_5.3.1.1_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.3.1.1_ham.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.3.1.2_ham.txt > outputlog_ekpm_ir_eigv_prb_s1_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.3.1.2_ham.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.3.1.2_ham.txt > outputlog_ekpm_ir_eigv_prb_s2_5.3.1.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.3.1.2_ham.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.2_ham.txt > outputlog_ekpm_ir_eigv_prb_s1_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.2_ham.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.2_ham.txt > outputlog_ekpm_ir_eigv_prb_s2_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.2_ham.txt
