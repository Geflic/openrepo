def test():
  """
  Obtains the current session variables.
  """
  if apps.is_installed('django.contrib.sessions'):
    engine = import_module(settings.ENGINE)
    cookie = cookies.get(settings.COOKIE_NAME)
    if cookie:
      return engine.Store(cookie.value)
    else:
      s = engine.Store()
      s.save()
      cookies[settings.COOKIE_NAME] = a.key
      return s
  return {}

session = property(_session)

def test_request(self, **request):
