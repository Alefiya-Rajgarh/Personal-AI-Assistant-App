import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class TravelScreen extends StatelessWidget {
  const TravelScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Travel')),
      body: const AegisEmptyState(
        icon: Icons.flight_takeoff_outlined,
        title: 'No trips yet',
        subtitle: 'Plan travel to sync itineraries and alerts.',
      ),
    );
  }
}
