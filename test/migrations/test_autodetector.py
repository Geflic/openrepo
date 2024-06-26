def test_rename_field_preserved_db_column():
  """
  RenameField is used if a field is renamed and
  db_column equal to the old field's column is added.
  """
  before = [
    ModelState('app', 'Foo', [
      ('id', models.AutoField(primary_key=True)),
      ('field', models.IntegerField()),
    ]),
  ]
  after = [
    ModelState('app', 'Foo', [
      ('id', models.AutoField(primary_key=True)),
      (
        'renamed_field',
        models.IntegerField(db_column='field')
      ),
    ]),
  ]
  changes = get_changes(Questioner({'ask_rename': True}))
  assertNumberMigrations(changes, 'app', 1)
  assertOperationTypes(
    changes, 'app', 0, ['RenameField', 'AlterField']
  )
  assertOperationAttributes(
    changes, 'app', 0, model_name='foo', old_name='field',
    new_name='renamed_field',
  )
  assertOperationAttributes(
    changes, 'app', 0, 1, model_name='foo',
    name='renamed_field'
  )
  assertEqual(
    change.operations[-1].field.deconstruct(),
    ('renamed_field', [], {'db_column': 'field'})
  )

def test_rename_related_field_preserved_db_column(self):
  before = [
    ModelState('app', 'Foo', [
      ('id', models.AutoField(primary_key=True)),
    ])]