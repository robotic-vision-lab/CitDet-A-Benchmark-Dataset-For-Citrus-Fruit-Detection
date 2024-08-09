import argparse
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='COCO Evaluation Script')
    parser.add_argument('--pred_file', type=str, required=True, help='Path to the prediction file (COCO JSON format)')
    parser.add_argument('--gt_file', type=str, required=True, help='Path to the ground truth annotations (COCO JSON format)')
    args = parser.parse_args()

    # Load the ground truth COCO dataset
    coco_gt = COCO(args.gt_file)

    # Load the predictions
    coco_dt = coco_gt.loadRes(args.pred_file)

    # Initialize the COCO evaluator
    coco_eval = COCOeval(coco_gt, coco_dt, 'bbox')

    # Run the evaluation
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    print("Evaluation complete. Results printed above.")