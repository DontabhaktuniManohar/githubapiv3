aws elbv2 modify-rule \
    --rule-arn <rule-arn> \
    --actions Type=forward,ForwardConfig='{"TargetGroups":[{"TargetGroupArn":"<target-group-arn-1>","Weight":100},{"TargetGroupArn":"<target-group-arn-2>","Weight":0}]}'
