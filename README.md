ASC code

第四题RELION 测试
首先，我们在RELION的编译上应用了一种混合编译，我们替换了不同的编译器来测试RELION，并将编译速度提高了8%。然后，充分利用现有的平台资源对RELION进行测试。我们扩展图像池并一次处理多个图像。为了利用我们的大RAM，我们通过管道提前读取图像。为了充分利用进程间的有效通信，我们禁止对进程级通信进行不必要的磁盘访问操作。最后，分析了RELION的核心算法。我们得到了3.3埃的解。
测试一 2D分类
代码：
mpirun -np 5 relion_refine_mpi --o Class2D/job007/ --i particles.star --ctf --iter 10 --tau2_fudge 2 --particle_diameter 150 --K 100 --flatten_solvent --zero_mask --strict_highres_exp 8 --oversampling 1 --psi_step 11.25 --offset_range 5 --offset_step 2 --norm --scale --gpu 0:1 --pool 100 --preread_images
测试二 3D分类cd 
代码：
mpirun -np 5 relion_refine_mpi --o Class3D/job007/ --i particles.star --ref run_ct24_class001.mrc --firstiter_cc --ini_high 40 --ctf --iter 40 --tau2_fudge 4 --particle_diameter 150 --K  4 --flatten_solvent --zero_mask --strict_highres_exp 10 --oversampling 1 --healpix_order 1 --sigma_ang 0.3 --offset_range 5 --offset_step 2 --sym O --norm --scale --scale --gpu --pooll 100 --preread_images > result_3d_class
测试三 3D重建
代码：
mpirun -np 5 relion_refine_mpi --o Step3.Refine3D/ --auto_refind --split_random_halves --i particles.star --ref run_ct24_class001.mrc --firstiter_cc --ini_high 40 -ctf -particle_diameter 150 --flatten_solvent --zero_mask --oversampling 1 --healpix_order 1 -- auto_local_healpix_order 5 --offset_range 5 --offset_step 2 --sym O --low_resol_join_halves 40 --norm --scale --gpu --free_gpu_memory 100 --pool 100 --preread_images > result_3d_refine

df -hl 查看当前磁盘剩余空间
Du -sh * 查看当前目录各个文件夹的总大小
ls -l 查看当前目录文件夹大小

xshell登录服务器以后往gpu结点传输文件：
scp -r /home/data_myname/file.txt  myname@gpu_ip:/home/gpu_myname
