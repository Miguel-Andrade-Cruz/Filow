def mapSchedules(schedules_obj):
    
    if schedules_obj == []:
        return False
    
    schedules_mapped = [
    {
      'teacher': schedule.teacher_id.user_id.name,
      'subject': schedule.subject_id.subject_name,
      'class': schedule.class_id.tag,
      'classroom_tag': schedule.classroom_id.tag,
      'classroom_quadrant': schedule.classroom_id.quadrant,
      'begins_at_time': schedule.begins_at_time,
      'ends_at_time': schedule.ends_at_time
    }
    for schedule in schedules_obj
    ]

    return schedules_mapped
