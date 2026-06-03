import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class HomeShellScreen extends StatelessWidget {
  const HomeShellScreen({super.key, required this.child});

  final Widget child;

  static const _tabs = [
    '/home',
    '/home/chat',
    '/home/calendar',
    '/home/tasks',
    '/home/travel',
    '/home/notifications',
  ];

  int _locationToIndex(String location) {
    for (var i = 0; i < _tabs.length; i++) {
      if (location.startsWith(_tabs[i])) {
        return i;
      }
    }
    return 0;
  }

  @override
  Widget build(BuildContext context) {
    final location = GoRouterState.of(context).matchedLocation;
    final currentIndex = _locationToIndex(location);

    return Scaffold(
      body: child,
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: currentIndex,
        type: BottomNavigationBarType.fixed,
        onTap: (index) => context.go(_tabs[index]),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home_outlined), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.chat_bubble_outline), label: 'Chat'),
          BottomNavigationBarItem(icon: Icon(Icons.calendar_today_outlined), label: 'Calendar'),
          BottomNavigationBarItem(icon: Icon(Icons.check_circle_outline), label: 'Tasks'),
          BottomNavigationBarItem(icon: Icon(Icons.flight_takeoff_outlined), label: 'Travel'),
          BottomNavigationBarItem(icon: Icon(Icons.notifications_outlined), label: 'Alerts'),
        ],
      ),
    );
  }
}
