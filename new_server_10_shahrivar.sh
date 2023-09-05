# finished

gwim default
simple
done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/gwim_default_normal_test.txt > outputlog_gwim_default_normal_test.txt 2>&1 &
tail --follow -n 10 results/gwim_default_normal_test.txt


done
ek ir gwim s1
python -u start.py -c "ekpm_ir_gwim_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ek_ir_gwim_s1.txt > outputlog_ek_ir_gwim_s1.txt 2>&1 &
tail --follow -n 10 results/ek_ir_gwim_s1.txt

done
ek ir gwim s2
python -u start.py -c "ekpm_ir_gwim_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ek_ir_gwim_s2.txt > outputlog_ek_ir_gwim_s2.txt 2>&1 &
tail --follow -n 10 results/ek_ir_gwim_s2.txt

done
ek ir eigv s1
python -u start.py -c "ekpm_ir_eigv_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_s1.txt > outputlog_ekpm_ir_eigv_s1.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s1.txt

done
ek ir eigv s2
python -u start.py -c "ekpm_ir_eigv_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_s2.txt > outputlog_ekpm_ir_eigv_s2.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_s2.txt


done
ekpm_ir_eigv_kshell_s1
python -u start.py -c "ekpm_ir_eigv_kshell_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_kshell_s1.txt > outputlog_ekpm_ir_eigv_kshell_s1.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_s1.txt


done
ekpm_ir_eigv_kshell_s2
python -u start.py -c "ekpm_ir_eigv_kshell_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_kshell_s2.txt > outputlog_ekpm_ir_eigv_kshell_s2.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_s2.txt

done
ekpm_ir_eigv_prb_s1
python -u start.py -c "ekpm_ir_eigv_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_prb_s1.txt > outputlog_ekpm_ir_eigv_prb_s1.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s1.txt


done
ekpm_ir_eigv_prb_s2
python -u start.py -c "ekpm_ir_eigv_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_prb_s2.txt > outputlog_ekpm_ir_eigv_prb_s2.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_prb_s2.txt


done
ekpm_ir_eigv_kshell_prb_s1
python -u start.py -c "ekpm_ir_eigv_kshell_prb_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_kshell_prb_s1.txt > outputlog_ekpm_ir_eigv_kshell_prb_s1.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_prb_s1.txt



git untill 06 50 am
git add results/gwim_default_normal_test.txt results/ek_ir_gwim_s1.txt results/ek_ir_gwim_s2.txt results/ekpm_ir_eigv_s1.txt results/ekpm_ir_eigv_s2.txt results/ekpm_ir_eigv_kshell_s1.txt results/ekpm_ir_eigv_kshell_s2.txt results/ekpm_ir_eigv_prb_s1.txt results/ekpm_ir_eigv_prb_s2.txt results/ekpm_ir_eigv_kshell_prb_s1.txt 


git add outputlog_ekpm_ir_eigv_kshell_prb_s1.txt outputlog_ekpm_ir_eigv_prb_s2.txt outputlog_ekpm_ir_eigv_prb_s1.txt outputlog_ekpm_ir_eigv_kshell_s2.txt outputlog_ekpm_ir_eigv_kshell_s1.txt outputlog_ekpm_ir_eigv_s2.txt outputlog_ekpm_ir_eigv_s1.txt outputlog_ek_ir_gwim_s2.txt outputlog_ek_ir_gwim_s1.txt outputlog_gwim_default_normal_test.txt



done
ekpm_default_s2
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s2.txt > outputlog_ekpm_default_s2.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2.txt


done
ekpm_ir_eigv_kshell_prb_s2
python -u start.py -c "ekpm_ir_eigv_kshell_prb_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_ir_eigv_kshell_prb_s2.txt > outputlog_ekpm_ir_eigv_kshell_prb_s2.txt 2>&1 &
tail --follow -n 10 results/ekpm_ir_eigv_kshell_prb_s2.txt


done
ekpm_default_s1
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s1.txt > outputlog_ekpm_default_s1.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1.txt

git add results/ekpm_default_s2.txt results/ekpm_default_s1.txt results/ekpm_ir_eigv_kshell_prb_s2.txt outputlog_ekpm_default_s2.txt outputlog_ekpm_ir_eigv_kshell_prb_s2.txt outputlog_ekpm_default_s1.txt


# tests execution








# article based exections
tests
done
python -u start.py -c "gwim_default" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/gwim_default_5.3.1.1.txt > outputlog_gwim_default_5.3.1.1.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.3.1.1.txt



# only this is under execution
done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/gwim_default_5.3.1.2.txt > outputlog_gwim_default_5.3.1.2.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.3.1.2.txt


# template
-----
not executed
name
python -u start.py -c "" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/.txt > outputlog_.txt 2>&1 &
tail --follow -n 10 results/.txt
----


done
python -u start.py -c "ekpm_default_s1" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s1_5.3.1.1.txt > outputlog_ekpm_default_s1_5.3.1.1.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.3.1.1.txt

done
python -u start.py -c "ekpm_default_s2" -kstart 10 -kstop 80 -kstep 10 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s2_5.3.1.1.txt > outputlog_ekpm_default_s2_5.3.1.1.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.3.1.1.txt



done
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s1_5.3.1.2.txt > outputlog_ekpm_default_s1_5.3.1.2.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.3.1.2.txt

done
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.01 -ppstop 0.1 -ppstep 10 -i 60 -am 0 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s2_5.3.1.2.txt > outputlog_ekpm_default_s2_5.3.1.2.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.3.1.2.txt