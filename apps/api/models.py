# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tabnanny import verbose
from django.db import models
from datetime import datetime


class ActivityLog(models.Model):
    id = models.IntegerField(primary_key=True)
    activity = models.CharField(max_length=250)
    user = models.CharField(max_length=125)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=125)

    def __str__(self):
        return str(self.activity) + ' - ' + str(self.created_date)

    class Meta:
        managed = False
        db_table = 'activity_log'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BusinessUnit(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Business Unit'
        verbose_name_plural = 'Business Units'
        managed = False
        db_table = 'business_unit'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mill(models.Model):
    mill_name = models.CharField(max_length=125)
    business_unit = models.ForeignKey(BusinessUnit, models.DO_NOTHING)

    def __str__(self):
        return self.mill_name

    class Meta:
        verbose_name = 'Mill'
        verbose_name_plural = 'Mills'
        managed = False
        db_table = 'mill'

# Not using this table
class PlantTasks(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    assigned_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=500, null=False)
    priority_level = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=150)
    image = models.TextField()
    image_complete = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'plant_tasks'


class Position(models.Model):
    name = models.CharField(max_length=250, blank=True, null=False)
    created_by = models.CharField(max_length=125)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
        managed = False
        db_table = 'position'


class Shifts(models.Model):
    name = models.CharField(max_length=150, blank=True, null=False)
    shift = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        managed = False
        db_table = 'shifts'

# Not using this table
class Subtasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=False)
    images_path = models.TextField(blank=True, null=True)
    assigned_to = models.IntegerField()
    assigned_date = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=125, blank=True, null=True)
    remarks = models.CharField(max_length=125)
    priority_level = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    plant_tasks = models.ForeignKey(PlantTasks, models.DO_NOTHING)
    created_date = models.DateField(blank=True, null=True)
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subtasks'



class User(models.Model):
    name = models.CharField(max_length=125)
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=125)
    email = models.CharField(max_length=125)
    contact = models.CharField(max_length=125)
    mill = models.ForeignKey(Mill, models.DO_NOTHING)
    position = models.ForeignKey(Position, models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        managed = False
        db_table = 'user'


class Task(models.Model):

    TYPE_CHOICES = (
        ('Incident', 'Incident'),
        ('Activity', 'Activity'),
    )

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
        ('Immediate', 'Immediate')
    )

    LOCATION_CHOICES = (
        ('Fresh palm fruit bunch reception section', 'Fresh palm fruit bunch reception section'),
        ('Sterilization section', 'Sterilization section'),
        ('Threshing section', 'Threshing section'),
        ('Digesting & pressing section', 'Digesting & pressing section'),
        ('Oilclarification section', 'Oilclarification section'),
        ('Fiber separation section', 'Fiber separation section'),
        ('Palm kernel recovery section', 'Palm kernel recovery section'),
        ('Engine room', 'Engine room'),
        ('Boiler house', 'Boiler house'),
        ('Water treatment', 'Water treatment'),
        ('Effulent Treatment Plant', 'Effulent Treatment Plant')

    )
    
    NAME_CHOICES = (
        ('Gervase Delmar Peck' , 'Gervase Delmar Peck'),
        ('Nirmala St John' ,'Nirmala Janeka St John'),
        ('Paulo Coelho' ,'Paulo Coelho'),
        ('Kole Marvyn Sharma' ,'Kole Marvyn Sharma'),
        ('Goh Yew King', 'Goh Yew King'),
        ('Aspen Isidora Polley', 'Aspen Isidora Polley'),
        ('Sid Jaron Hull' , 'Sid Jaron Hull'),
        ('Ahyani Siregar' , 'Ahyani Siregar'),
        ('George Siregar' , 'George Siregar'),
        ('Tony Eusoff' ,'Tony Eusoff'),
        ('Xu Rongmao' ,'Xu Rongmao'),
        ('Liliyana Natsir' ,'Liliyana Natsir'),
        ('Andrea Hirata' ,'Andrea Hirata'),
        ('Revalina Sayuthi Temat','Revalina Sayuthi Temat' )
    )
    


    task = models.CharField(max_length=500, blank=True, null=True)
    assigned_to = models.CharField(max_length=500, null=True, blank = True, choices=NAME_CHOICES)
    assigned_date = models.DateTimeField(blank=True, null=True)
    shift = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateTimeField(default=datetime.now(),blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=250, blank=True, null=False, choices = LOCATION_CHOICES)
    comment = models.TextField( blank=True, null=True)
    remarks = models.TextField( blank=True, null=True)
    progress = models.CharField(max_length=250, blank=True, null=True)
    photo = models.TextField( blank=True, null=True)
    photo_varying = models.TextField( blank=True, null=True)
    assigned_by = models.CharField(max_length=500, blank=True, null=True, choices=NAME_CHOICES)
    is_handover = models.BooleanField(null=True)
    created_by = models.CharField(max_length=500, blank=True, null=False)
    created_date = models.DateTimeField(blank=True, null=True)
    priority_level = models.CharField(max_length=250, blank=True, null=False, choices=PRIORITY_CHOICES)
    type = models.CharField(max_length=250, blank=True, null=False, choices=TYPE_CHOICES)
    mill = models.ForeignKey(Mill, on_delete=models.CASCADE, null=True)
    time_incident = models.DateTimeField(blank=True, null=True)

    
    def __str__(self):
        return str(self.task)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        managed = False
        db_table = 'task'

class TaskHandover(models.Model):
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    handover_date = models.DateTimeField()
    handover_pic = models.CharField(max_length=125)
    handover_remark = models.TextField()
    handover_assigned_by = models.IntegerField()
    created_by = models.CharField(max_length=125)
    created_date = models.DateTimeField()

    def __str__(self):
        return "[HANDOVER] " + str(self.task)

    class Meta:
        verbose_name = 'Handover'
        verbose_name_plural = 'Handovers'
        managed = False
        db_table = 'task_handover'

# Not using this table
class TaskHandoverBackup(models.Model):
    task_incident = models.ForeignKey('TaskIncident', models.DO_NOTHING)
    shifted_date = models.DateTimeField()
    shifted_pic = models.CharField(max_length=125)
    shifted_remark = models.CharField(max_length=125)
    old_assigned_date = models.DateTimeField()
    old_remark = models.CharField(max_length=120)
    created_by = models.CharField(max_length=125)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_handover_backup'

# Not using this table
class TaskIncident(models.Model):
    subtasks = models.ForeignKey(Subtasks, models.DO_NOTHING, blank=True, null=True)
    plant_tasks = models.ForeignKey(PlantTasks, models.DO_NOTHING, blank=True, null=True)
    incident_id = models.IntegerField()
    incident_by = models.IntegerField()
    type = models.CharField(max_length=125)
    location = models.CharField(max_length=125)
    assigned_to = models.IntegerField()
    priority = models.CharField(max_length=125)
    remark = models.CharField(max_length=125)
    comment = models.CharField(max_length=125)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    due_date = models.DateTimeField()
    completion_status = models.CharField(max_length=125)
    is_handover = models.BooleanField()
    image_path = models.CharField(max_length=125)
    manager_verified = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=125)

    class Meta:
        managed = False
        db_table = 'task_incident'

