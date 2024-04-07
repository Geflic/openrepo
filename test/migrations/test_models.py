migrations.CreateModel(
  name="IntegerArrayModel",
  fields=[
    (
      "id",
      m.AutoField(
        verbose_name="ID",
        serialize=False,
        auto_created=True,
        primary_key=True,
      ),
    ),
    (
      "field",
      ArrayField(
        m.IntegerField(), blank=True,
        default=list, size=None
      ),
    ),
  ],
  options={
    "required_db_vendor": "postgresql",
  },
  bases=(m.Model,),
)