
# 5.2
# astro

done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 1 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/gwim_default_5.2.txt > outputlog_gwim_default_5.2.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.2.txt

done
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 1 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s1_5.2.txt > outputlog_ekpm_default_s1_5.2.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.2.txt

done
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.02 -i 60 -am 1 -vdl 2 -d "./dataset/CA-AstroPh3.tsv" | tee results/ekpm_default_s2_5.2.txt > outputlog_ekpm_default_s2_5.2.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.2.txt


# ham
done
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/gwim_default_5.2_ham.txt > outputlog_gwim_default_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.2_ham.txt

done x
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s1_5.2_ham.txt > outputlog_ekpm_default_s1_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.2_ham.txt

done x
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.03 -i 60 -am 1 -vdl 2 -d "./dataset/out.petster-hamster.tsv" | tee results/ekpm_default_s2_5.2_ham.txt > outputlog_ekpm_default_s2_5.2_ham.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.2_ham.txt


# pgp
done x
python -u start.py -c "gwim_default" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/gwim_default_5.2_pgp.txt > outputlog_gwim_default_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/gwim_default_5.2_pgp.txt

done x
python -u start.py -c "ekpm_default_s1" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_default_s1_5.2_pgp.txt > outputlog_ekpm_default_s1_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s1_5.2_pgp.txt

done x
python -u start.py -c "ekpm_default_s2" -kstart 20 -m 100 -ps 25 -t 50 -ppstart 0.06 -i 60 -am 1 -vdl 2 -d "./dataset/out.arenas-pgp.tsv" | tee results/ekpm_default_s2_5.2_pgp.txt > outputlog_ekpm_default_s2_5.2_pgp.txt 2>&1 &
tail --follow -n 10 results/ekpm_default_s2_5.2_pgp.txt