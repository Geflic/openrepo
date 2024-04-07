def test():
  """
  Obtains the current session variables.
  """
  engine = import_module(settings.ENGINE)
  cookie = cookies.get(settings.COOKIE_NAME)
  if cookie:
    return engine.Store(cookie.value)

  session = engine.Store()
  session.save()
  cookies[settings.COOKIE_NAME] = session.key
  return session

session = property(_session)

def test_request(self, **request):