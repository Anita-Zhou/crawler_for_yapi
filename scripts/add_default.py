import json

# # Original file name
# filename = "test1"
# pre_dir = "./texts/"
# post_dir = "./updated_texts/"
# # File names
# input_file = pre_dir + filename + ".txt"
# output_file = post_dir+ filename + "_alter.txt"


def default_helper(p_key, key, value):
    if "default" not in value:
        default_value = "新建默认值"
        # print(parameter_key)
        match key:
            case "id":
                default_value = "键id"
            case "pid":
                default_value = "父id"
            case "parentId":
                default_value = "父id"
            case "name":
                default_value = "名称"
                if p_key == "prodCategories":
                    default_value = "项目" + default_value
            case "type":
                default_value = "类型"
                if p_key == "prodCategories":
                    default_value = "项目" + default_value
                else:
                    default_value = " "
                #TODO: Add more kind of situations here
            case "description":
                default_value = "详情"
            case "seq":
                default_value = "第几次/排序"
            case "courseNum":
                default_value = "参加课程数量"
            case "createTime":
                default_value = "创建时间"
            case "updateTime":
                default_value = "更新时间"
            case "totalDuration":
                default_value = "总持续时间"
            case "delayDays":
                default_value = "计划延迟时间"
            case "status":
                default_value = "状态"
            case "businessType":
                default_value = "业务类型"
            case "times":
                default_value = "次数"
            case "groups":
                default_value = "组数"
            case "batch":
                default_value = "组数"
            case "span":
                default_value = "平均心率"
            case "force":
                default_value = "总力量（当且仅当存在无氧运动时大于0）"
            case "calorie":
                default_value = "训练卡路里"
            case "trainTime":
                default_value = "训练时间"
            case "avgHeartRate":
                default_value = "平津心率"
            case "avgBloodOxygen":
                default_value = "平均血氧"
            case "heartRate":
                default_value = "心率"
            case "bloodOxygen":
                default_value = "血氧"
            case "leftForce":
                default_value = "左边拉力"
            case "rightForce":
                default_value = "右边拉力"
            case "leftLength":
                default_value = "左边距离"
            case "rightLength":
                default_value = "右边距离"
            case "leftForceMode":
                default_value = "左边力量模式"
            case "rightForceMode":
                default_value = "右边力量模式"
            case "power" :
                default_value = "power"
            case "index":
                default_value = "目录/指数"
            case "weight":
                default_value = "体重"
            case "height":
                default_value = "身高"
            case "total":
                default_value = "身高"
            case "useMachine":
                default_value = "是否使用机器"
            case "current":
                default_value = "当前页"
            case "searchCount":
                default_value = "搜索量"
            case "hitCount":
                default_value = "点击量"
            case "pages":
                default_value = "页面数"
            case "size":
                default_value = "每页显示条数，默认 10"
            case "icon":
                default_value = "图标"
            case "menuType":
                default_value = "菜单类型"
            case "createBy":
                default_value = "创建人"
            case "updateBy":
                default_value = "修改人"
            case "contentType":
                default_value = "内容类型"
            case  "directory":
                default_value = "所属文件夹"
            case "extension":
                default_value = "拓展名"
            case "timesDelta":
                default_value = "时间差"
            case "powerDelta":
                default_value = "力量差"
            case "groups":
                default_value = "组数"
            case "diet":
                default_value = "饮食计划"
            case "rest":
                default_value = "休息时长/次数（具体询问后端）"
            case "dayNum":
                default_value = "总天数/第几天"
            case "dayNums":
                default_value = "总天数"
            case "weekDayNum":
                default_value = "工作日天数"
            case "startTime":
                default_value = "开始时间"
            case "endTime":
                default_value = "结束时间"
            case "planTrainTime":
                default_value = "计划训练时间"
            case "auditStatus":
                default_value = "审核状态"
            case "auditTime":
                default_value = "审核时间"
            case "registerTime":
                default_value = "注册时间"
            case "trainNum":
                default_value = "训练序号"
            case "recentSignTime":
                default_value = "上次打卡时间"
            case "consecutiveNum":
                default_value = "连续打卡天数"
            case "totalSign":
                default_value = "总签到天数"
            case "totalPersonNum":
                default_value = "总打卡人数"
            case "rank":
                default_value = "排名"
            case "likeAmount":
                default_value = "点赞量"
            case "showLocation":
                default_value = "广告展示位置"
            case "trainCalorie":
                default_value = "训练卡路里"
            case "aerobic":
                default_value = "有氧类型"
            case "aerobicCalorie":
                default_value = "有氧卡路里"
            case "anaerobicCalorie":
                default_value = "无氧卡路里"
            case "aerobicTime":
                default_value = "有氧时间"
            case "anaerobicTime":
                default_value = "无氧时间"
            case "sumAerobicTime":
                default_value = "总有氧时间"
            case "sumAnaerobicTime":
                default_value = "总无氧时间"
            case "sumAerobicCalorie":
                default_value = "总有氧卡路里"
            case "sumAnaerobicCalorie":
                default_value = "总无氧卡路里"
            case "sumTimes":
                default_value = "总次数"
            case "sumForce":
                default_value = "总力量"
            case "tugOfWarWin":
                default_value = "拔河比赛胜利次数"
            case "tugOfWarDefeat":
                default_value = "拔河比赛失败次数"
            case "tugOfWarTie":
                default_value = "拔河比赛平局次数"
            case "tugOfWarRank": 
                default_value = "拔河比赛排名"
            case "canoeAndKayakTimes":
                default_value = "皮划艇次数"
            case "canoeAndKayakRank":
                default_value = "皮划艇排名"
            case "useNumber":
                default_value = "用户号码/使用量（具体询问后端）"
            case "result":
                default_value = "结果"
            case "gnameUpdateTime":
                default_value = "gname上次更改时间"
            case "gnameUpdateCount":
                default_value = "gname总更改次数"
            case "participationPeopleNumber":
                default_value = "参与人数"
            case "trainingTime":
                default_value = "训练时间"
            case "totalCapacity":
                default_value = "总消耗"
            case "totalCalorie":
                default_value = "总卡路里"
            case "doneLessons":
                default_value = "已完成课程"
            case "totalLessons":
                default_value = "总课程"
            case "doneDay":
                default_value = "完成日期"
            case "totalDay":
                default_value = "总日期"
            case "messageType":
                default_value = "消息类型(01:系统 02游戏, 03训练结果, 04点赞,05评论,06关注,07课堂通知,08计划通知, 09 举报文章成功/失败, 10举报用户成功/失败, 11动态举报后被下架)"
            case "comment":
                default_value = "评论/回复内容"
            case "favor":
                default_value = "点赞"
            case "fans":
                default_value = "新增粉丝"
            case "count":
                default_value = "数量"
            case "duration":
                default_value = "持续时间"
            case "fileSize":
                default_value = "文件大小"
            case "deviceId":
                default_value = "设备id"
            case "grade":
                default_value = "健身经验等级 01:初级 02:中级 03:高级"
            case "prodCategory":
                default_value = "配件信息"
            case "classRoomUser":
                default_value = "预约用户信息"
            case "pepdId":
                default_value = "1v1私教计划包明细id"
            case "planId":
                default_value = "计划id"
            case "volume":
                default_value = " "
            case "reachValue":
                default_value = " "
            case "daySeq":
                default_value = " "
            case "end":
                default_value = "是否结束"
            case _:
                if "id" or "Id" in key:
                    default_value = " "
                else:
                    # Default case: Specify the default value or action here
                    default_value = "新建默认值"

        # print("key:" + str(key))
        value["default"] = default_value
    

def set_default(p_key, param_key, param_val):
    # print("====== set_default called with key: " + str(param_key) + ", val :" + str(param_val) + " ======")
    print("DEBUG: val :" + str(param_val))
    if param_val["type"] == "array":
        # #DEBUG
        print(str(param_val) + " has the type array\n")

        val_objs = param_val["items"]
        if "properties" in val_objs.keys():
            val_objs = val_objs["properties"]
            for val_k, val_v in val_objs.items():
                set_default(param_key, val_k, val_v)

    elif param_val["type"] == "object":
        # #DEBUG
        print(str(param_key) + " has the type object\n")

        val_objs = param_val["properties"]
        for val_k, val_v in val_objs.items():
            set_default(param_key, val_k, val_v)
    else:
        #  #DEBUG
        # print(str(param_val) + " is a usual type\n")
        default_helper(p_key, param_key, param_val)


        
# # Read JSON string from input file
# with open(input_file, 'r') as file:
#     json_string = file.read()

# # Parse JSON string into a JSON object
# json_object = json.loads(json_string)

# # Modify the JSON object as desired
# if "value" in json_object["properties"].keys():
#     val_obj = json_object["properties"]["value"]
#     set_default("root", "value", val_obj)
#     # if(val_obj["type"] == "array"):
#     #  = json_object["properties"]["value"]["properties"]

#     # # Check whether the default helper is working
#     # res = 0
#     # for parameter_key, parameter_value in value_object.items():
#     #     set_default(parameter_key, parameter_value)

# # Convert the JSON object back to a JSON string
# updated_json_string = json.dumps(json_object, indent=2, ensure_ascii=False)

# # Write the JSON string to the output file
# with open(output_file, 'w') as file:
#     file.write(updated_json_string)