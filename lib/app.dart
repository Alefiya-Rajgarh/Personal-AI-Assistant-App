import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'core/router/app_router.dart';
import 'core/theme/aegis_theme.dart';
import 'core/providers/auth_provider.dart';

class App extends ConsumerWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final isAuthenticated = ref.watch(authStateProvider);

    return MaterialApp.router(
      title: 'Assistant AI',
      theme: AegisTheme.lightTheme,
      darkTheme: AegisTheme.darkTheme,
      themeMode: ThemeMode.dark,
      routerConfig: AppRouter.router(isAuthenticated: isAuthenticated),
      debugShowCheckedModeBanner: false,
    );
  }
}
