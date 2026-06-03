import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class CalendarScreen extends StatelessWidget {
  const CalendarScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Calendar')),
      body: AegisEmptyState(
        icon: Icons.calendar_today_outlined,
        title: 'No events synced',
        subtitle: 'Connect your calendar to see meetings here.',
        ctaLabel: 'View demo event',
        onCtaPressed: () => context.go('/home/calendar/preview'),
      ),
    );
  }
}
