# pgp ekpm_ir_gwim
!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s1_5.3.1.1_pgp.txt > outputlog_ekpm_ir_gwim_s1_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.3.1.1_pgp.txt

!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s2_5.3.1.1_pgp.txt > outputlog_ekpm_ir_gwim_s2_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.3.1.1_pgp.txt



!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s1_5.3.1.2_pgp.txt > outputlog_ekpm_ir_gwim_s1_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.3.1.2_pgp.txt

!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s2_5.3.1.2_pgp.txt > outputlog_ekpm_ir_gwim_s2_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.3.1.2_pgp.txt


!done
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s1_5.2_pgp.txt > outputlog_ekpm_ir_gwim_s1_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s1_5.2_pgp.txt


!done
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_gwim_s2_5.2_pgp.txt > outputlog_ekpm_ir_gwim_s2_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_gwim_s2_5.2_pgp.txt


# pgp ekpm_ir_eigv
!done
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s1_5.3.1.1_pgp.txt > outputlog_ekpm_ir_eigv_s1_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.3.1.1_pgp.txt

!done
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s2_5.3.1.1_pgp.txt > outputlog_ekpm_ir_eigv_s2_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.3.1.1_pgp.txt



!done
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s1_5.3.1.2_pgp.txt > outputlog_ekpm_ir_eigv_s1_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.3.1.2_pgp.txt

!done
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s2_5.3.1.2_pgp.txt > outputlog_ekpm_ir_eigv_s2_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.3.1.2_pgp.txt


python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s1_5.2_pgp.txt > outputlog_ekpm_ir_eigv_s1_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1_5.2_pgp.txt


python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_s2_5.2_pgp.txt > outputlog_ekpm_ir_eigv_s2_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2_5.2_pgp.txt


# pgp ekpm_ir_eigv_prb
!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.3.1.1_pgp.txt > outputlog_ekpm_ir_eigv_prb_s1_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.3.1.1_pgp.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.3.1.1_pgp.txt > outputlog_ekpm_ir_eigv_prb_s2_5.3.1.1_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.3.1.1_pgp.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.3.1.2_pgp.txt > outputlog_ekpm_ir_eigv_prb_s1_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.3.1.2_pgp.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.3.1.2_pgp.txt > outputlog_ekpm_ir_eigv_prb_s2_5.3.1.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.3.1.2_pgp.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s1_5.2_pgp.txt > outputlog_ekpm_ir_eigv_prb_s1_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1_5.2_pgp.txt


!done
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_ir_eigv_prb_s2_5.2_pgp.txt > outputlog_ekpm_ir_eigv_prb_s2_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2_5.2_pgp.txt
