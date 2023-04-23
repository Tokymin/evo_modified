# 对齐两条轨迹并把对齐后的结果写入csv文件
# # 调用evo计算APE等
from evo import entry_points
from evo import main_rpe
import argcomplete

model_prefix="SC_Depthv1"
main_rpe.est_file = r"source/SC_Depthv1.kitti"
main_rpe.ref_file = "source/Ground_Truth.kitti"
main_rpe.model_prefix = model_prefix

main_rpe.rpe_metric_csv_path = r"save_metric/RPE_metric" + model_prefix + ".csv"  # 保存csv的文件
main_rpe.ape_metric_csv_path = r"save_metric/APE_metric" + model_prefix + ".csv"
main_rpe.modified_csv_path = r"save_align/save_align_traj" + model_prefix + ".csv"

parser = main_rpe.parser()
argcomplete.autocomplete(parser)
entry_points.launch(main_rpe, parser)