import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../features/auth/presentation/screens/login_screen.dart';
import '../../features/auth/presentation/screens/register_screen.dart';
import '../../features/auth/presentation/screens/splash_screen.dart';
import '../../features/auth/presentation/screens/onboarding_screen.dart';
import '../../features/home/presentation/screens/home_shell_screen.dart';
import '../../features/home/presentation/screens/home_screen.dart';
import '../../features/chat/presentation/screens/chat_screen.dart';
import '../../features/calendar/presentation/screens/calendar_screen.dart';
import '../../features/calendar/presentation/screens/calendar_detail_screen.dart';
import '../../features/tasks/presentation/screens/tasks_screen.dart';
import '../../features/tasks/presentation/screens/task_detail_screen.dart';
import '../../features/travel/presentation/screens/travel_screen.dart';
import '../../features/notifications/presentation/screens/notifications_screen.dart';
import '../../features/memory/presentation/screens/memory_screen.dart';
import '../../features/settings/presentation/screens/settings_screen.dart';
import '../../features/settings/presentation/screens/settings_preferences_screen.dart';
import '../../features/settings/presentation/screens/settings_integrations_screen.dart';
import '../../features/subscription/presentation/screens/subscription_screen.dart';

class AppRouter {
  static GoRouter router({required bool isAuthenticated}) {
    return GoRouter(
      initialLocation: '/splash',
      redirect: (context, state) {
        final isAuthRoute = state.matchedLocation.startsWith('/auth');
        final isSplashOrOnboarding = state.matchedLocation == '/splash' ||
            state.matchedLocation == '/onboarding';

        if (!isAuthenticated && !isAuthRoute && !isSplashOrOnboarding) {
          return '/auth/login';
        }
        if (isAuthenticated && isAuthRoute) {
          return '/home';
        }
        return null;
      },
      routes: [
        GoRoute(
          path: '/splash',
          builder: (context, state) => const SplashScreen(),
        ),
        GoRoute(
          path: '/onboarding',
          builder: (context, state) => const OnboardingScreen(),
        ),
        GoRoute(
          path: '/auth/login',
          builder: (context, state) => const LoginScreen(),
        ),
        GoRoute(
          path: '/auth/register',
          builder: (context, state) => const RegisterScreen(),
        ),
        ShellRoute(
          builder: (context, state, child) => HomeShellScreen(child: child),
          routes: [
            GoRoute(
              path: '/home',
              builder: (context, state) => const HomeScreen(),
              routes: [
                GoRoute(
                  path: 'chat',
                  builder: (context, state) => const ChatScreen(),
                ),
                GoRoute(
                  path: 'calendar',
                  builder: (context, state) => const CalendarScreen(),
                  routes: [
                    GoRoute(
                      path: ':id',
                      builder: (context, state) => CalendarDetailScreen(
                        eventId: state.pathParameters['id'] ?? '',
                      ),
                    ),
                  ],
                ),
                GoRoute(
                  path: 'tasks',
                  builder: (context, state) => const TasksScreen(),
                  routes: [
                    GoRoute(
                      path: ':id',
                      builder: (context, state) => TaskDetailScreen(
                        taskId: state.pathParameters['id'] ?? '',
                      ),
                    ),
                  ],
                ),
                GoRoute(
                  path: 'travel',
                  builder: (context, state) => const TravelScreen(),
                ),
                GoRoute(
                  path: 'notifications',
                  builder: (context, state) => const NotificationsScreen(),
                ),
              ],
            ),
          ],
        ),
        GoRoute(
          path: '/memory',
          builder: (context, state) => const MemoryScreen(),
        ),
        GoRoute(
          path: '/settings',
          builder: (context, state) => const SettingsScreen(),
          routes: [
            GoRoute(
              path: 'preferences',
              builder: (context, state) => const SettingsPreferencesScreen(),
            ),
            GoRoute(
              path: 'integrations',
              builder: (context, state) => const SettingsIntegrationsScreen(),
            ),
          ],
        ),
        GoRoute(
          path: '/subscription',
          builder: (context, state) => const SubscriptionScreen(),
        ),
      ],
      errorBuilder: (context, state) => Scaffold(
        body: Center(child: Text('Route not found: ${state.uri}')),
      ),
    );
  }
}
