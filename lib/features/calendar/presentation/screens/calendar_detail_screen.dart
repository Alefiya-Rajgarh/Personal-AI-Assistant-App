import 'package:flutter/material.dart';

import '../../../../core/theme/aegis_spacing.dart';
import '../../../../core/widgets/aegis_card.dart';

class CalendarDetailScreen extends StatelessWidget {
  const CalendarDetailScreen({super.key, required this.eventId});

  final String eventId;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Event $eventId')),
      body: Padding(
        padding: const EdgeInsets.all(AssistanceSpacing.lg),
        child: const AegisCard(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Strategy sync'),
              SizedBox(height: AssistanceSpacing.sm),
              Text('10:00 AM • Executive boardroom'),
            ],
          ),
        ),
      ),
    );
  }
}
